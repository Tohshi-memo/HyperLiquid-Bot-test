# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T21:52:30.117979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9087` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.889` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.7481` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.5486` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.1887` n `234`; crypto_major avg `-0.1179` n `8`; equity avg `-0.0215` n `137`; fx avg `0.0001` n `6`; index avg `0.0018` n `27`; metal avg `0.0142` n `20`; unknown avg `3.349` n `903`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.5862` n `234`; crypto_major avg `-0.4887` n `8`; equity avg `-0.1621` n `137`; fx avg `-0.0049` n `6`; index avg `-0.0061` n `27`; metal avg `0.009` n `20`; unknown avg `2.9836` n `893`
- 4h: commodity avg `-0.1099` n `12`; crypto_alt avg `-2.7019` n `234`; crypto_major avg `-2.858` n `8`; equity avg `-0.3094` n `137`; fx avg `-0.0124` n `6`; index avg `0.031` n `27`; metal avg `0.0507` n `20`; unknown avg `1.381` n `868`
- 24h: commodity avg `0.4718` n `12`; crypto_alt avg `-4.3885` n `234`; crypto_major avg `-4.9413` n `8`; equity avg `-1.3035` n `137`; fx avg `0.1982` n `6`; index avg `-0.0775` n `27`; metal avg `0.1585` n `20`; unknown avg `2.1177` n `818`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
