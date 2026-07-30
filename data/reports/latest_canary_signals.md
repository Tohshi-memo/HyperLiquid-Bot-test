# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T04:37:31.132418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0283` n `230`; crypto_major avg `0.0625` n `8`; equity avg `0.122` n `102`; fx avg `-0.0178` n `6`; index avg `0.0516` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0243` n `779`
- 1h: commodity avg `0.0451` n `12`; crypto_alt avg `-0.1523` n `230`; crypto_major avg `-0.1635` n `8`; equity avg `-0.0801` n `102`; fx avg `-0.0497` n `6`; index avg `0.0412` n `25`; metal avg `-0.0136` n `20`; unknown avg `0.1753` n `779`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `0.4892` n `230`; crypto_major avg `0.1494` n `8`; equity avg `-0.4432` n `102`; fx avg `-0.0288` n `6`; index avg `0.0593` n `25`; metal avg `-0.1694` n `20`; unknown avg `0.2874` n `778`
- 24h: commodity avg `0.5176` n `12`; crypto_alt avg `-0.0663` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `-1.3288` n `102`; fx avg `0.08` n `6`; index avg `0.0844` n `25`; metal avg `0.1162` n `20`; unknown avg `-0.4818` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
