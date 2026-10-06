# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T20:37:28.062072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `13`; crypto_alt avg `-0.1608` n `235`; crypto_major avg `-0.0295` n `8`; equity avg `0.0377` n `150`; fx avg `-0.0008` n `6`; index avg `0.0007` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.0943` n `1074`
- 1h: commodity avg `0.0621` n `13`; crypto_alt avg `0.2368` n `235`; crypto_major avg `0.2399` n `8`; equity avg `0.1401` n `150`; fx avg `-0.0041` n `6`; index avg `0.0094` n `26`; metal avg `-0.0217` n `20`; unknown avg `8.2018` n `1012`
- 4h: commodity avg `0.3632` n `13`; crypto_alt avg `-0.2546` n `235`; crypto_major avg `-0.0484` n `8`; equity avg `-0.1966` n `150`; fx avg `0.0005` n `6`; index avg `-0.0735` n `26`; metal avg `0.0517` n `20`; unknown avg `7.0536` n `1012`
- 24h: commodity avg `0.319` n `13`; crypto_alt avg `-0.999` n `235`; crypto_major avg `-0.6675` n `8`; equity avg `0.3873` n `149`; fx avg `0.1001` n `6`; index avg `-0.0199` n `26`; metal avg `0.0459` n `20`; unknown avg `867.5195` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
