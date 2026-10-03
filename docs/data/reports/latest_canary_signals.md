# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T07:07:29.470860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0229` n `13`; crypto_alt avg `-0.1299` n `235`; crypto_major avg `-0.0827` n `8`; equity avg `0.014` n `143`; fx avg `0.0108` n `6`; index avg `0.003` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0716` n `982`
- 1h: commodity avg `0.0515` n `13`; crypto_alt avg `-0.1296` n `235`; crypto_major avg `-0.0918` n `8`; equity avg `0.0162` n `143`; fx avg `0.0026` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.1023` n `982`
- 4h: commodity avg `-0.0422` n `13`; crypto_alt avg `0.0543` n `235`; crypto_major avg `0.0` n `8`; equity avg `-0.0431` n `143`; fx avg `-0.0025` n `6`; index avg `-0.0122` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.1864` n `954`
- 24h: commodity avg `0.2088` n `13`; crypto_alt avg `-1.5224` n `235`; crypto_major avg `-1.9016` n `8`; equity avg `0.4395` n `142`; fx avg `-0.0412` n `6`; index avg `0.2163` n `26`; metal avg `-0.2749` n `20`; unknown avg `-0.9288` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
