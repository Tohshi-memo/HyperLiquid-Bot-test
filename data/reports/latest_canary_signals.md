# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T02:07:28.065430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.0461` n `8`; equity avg `-0.1668` n `102`; fx avg `-0.0138` n `6`; index avg `-0.0319` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0102` n `779`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.5692` n `230`; crypto_major avg `0.4912` n `8`; equity avg `0.472` n `102`; fx avg `0.0445` n `6`; index avg `0.1742` n `25`; metal avg `0.0043` n `20`; unknown avg `0.2794` n `779`
- 4h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.9584` n `230`; crypto_major avg `0.6724` n `8`; equity avg `1.9452` n `102`; fx avg `0.0109` n `6`; index avg `0.4409` n `25`; metal avg `0.1591` n `20`; unknown avg `0.9151` n `778`
- 24h: commodity avg `0.4043` n `12`; crypto_alt avg `-0.6288` n `230`; crypto_major avg `0.4823` n `8`; equity avg `-1.1124` n `102`; fx avg `0.058` n `6`; index avg `0.0292` n `25`; metal avg `0.4356` n `20`; unknown avg `-0.5425` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
