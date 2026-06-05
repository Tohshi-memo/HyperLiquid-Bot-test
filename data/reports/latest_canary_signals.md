# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T06:41:50.743338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.378` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.3215` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.2547` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.5251` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.3658` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.3032` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.2295` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-1.5429` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.4345` n `228`; crypto_major avg `0.6111` n `8`; equity avg `-0.0787` n `74`; fx avg `-0.0373` n `6`; index avg `0.0548` n `23`; metal avg `0.4303` n `18`; unknown avg `0.9015` n `424`
- 1h: commodity avg `-0.145` n `12`; crypto_alt avg `-3.2885` n `228`; crypto_major avg `-2.3745` n `8`; equity avg `-0.8316` n `74`; fx avg `-0.0003` n `6`; index avg `-0.0713` n `23`; metal avg `-0.0087` n `18`; unknown avg `-1.0437` n `404`
- 4h: commodity avg `-0.1333` n `12`; crypto_alt avg `-4.0992` n `228`; crypto_major avg `-3.4548` n `8`; equity avg `-0.9297` n `74`; fx avg `-0.0375` n `6`; index avg `-0.2001` n `23`; metal avg `-0.0768` n `18`; unknown avg `-1.481` n `404`
- 24h: commodity avg `-0.0971` n `12`; crypto_alt avg `-8.2076` n `228`; crypto_major avg `-6.7279` n `8`; equity avg `-2.1289` n `73`; fx avg `0.1393` n `6`; index avg `-0.5619` n `23`; metal avg `-0.4852` n `18`; unknown avg `-1.5162` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
