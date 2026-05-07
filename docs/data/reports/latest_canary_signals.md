# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T09:37:23.690865+00:00`
- Correlation status: `ready`
- Asset price records: `538`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1106` n `12`; crypto_alt avg `-0.1677` n `228`; crypto_major avg `0.0059` n `8`; equity avg `0.0673` n `65`; fx avg `-0.0012` n `4`; index avg `-0.0755` n `23`; metal avg `0.1583` n `18`; unknown avg `-0.0218` n `358`
- 1h: commodity avg `-0.2741` n `12`; crypto_alt avg `-0.1518` n `228`; crypto_major avg `-0.1997` n `8`; equity avg `0.2708` n `65`; fx avg `0.063` n `4`; index avg `-0.1113` n `23`; metal avg `0.1199` n `18`; unknown avg `-0.0802` n `358`
- 4h: commodity avg `-1.0021` n `12`; crypto_alt avg `0.439` n `228`; crypto_major avg `0.2097` n `8`; equity avg `0.4442` n `65`; fx avg `0.0636` n `4`; index avg `0.0454` n `23`; metal avg `1.1631` n `18`; unknown avg `0.2783` n `356`
- 24h: commodity avg `-0.7669` n `7`; crypto_alt avg `0.1378` n `223`; crypto_major avg `-1.7999` n `7`; equity avg `0.5036` n `47`; fx avg `0.1176` n `4`; index avg `0.5322` n `6`; metal avg `1.4796` n `7`; unknown avg `0.8857` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1303`, n `534`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `534`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `534`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0813`, n `530`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `530`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.077`, n `530`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `530`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `530`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `530`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `534`, weak_sample_signal
