# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T04:52:25.142122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0074` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3813` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0779` n `12`; crypto_alt avg `0.2037` n `228`; crypto_major avg `0.2836` n `8`; equity avg `-0.0177` n `74`; fx avg `0.0119` n `6`; index avg `-0.0352` n `23`; metal avg `0.0228` n `18`; unknown avg `0.0091` n `517`
- 1h: commodity avg `0.2207` n `12`; crypto_alt avg `-0.6603` n `228`; crypto_major avg `-0.5857` n `8`; equity avg `-0.316` n `74`; fx avg `0.0066` n `6`; index avg `-0.1669` n `23`; metal avg `-0.0306` n `18`; unknown avg `-0.0657` n `517`
- 4h: commodity avg `0.4978` n `12`; crypto_alt avg `-1.7933` n `228`; crypto_major avg `-1.5096` n `8`; equity avg `-0.4951` n `74`; fx avg `0.0099` n `6`; index avg `-0.1283` n `23`; metal avg `-0.5934` n `18`; unknown avg `-0.0838` n `517`
- 24h: commodity avg `0.5976` n `12`; crypto_alt avg `0.476` n `228`; crypto_major avg `2.3626` n `8`; equity avg `1.1328` n `74`; fx avg `-0.087` n `6`; index avg `0.1048` n `23`; metal avg `-0.2712` n `18`; unknown avg `-5.5672` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
