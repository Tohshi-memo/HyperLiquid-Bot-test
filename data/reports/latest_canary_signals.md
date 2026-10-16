# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T04:52:30.122691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0288` n `236`; crypto_major avg `-0.0114` n `8`; equity avg `0.148` n `151`; fx avg `-0.0014` n `6`; index avg `0.0209` n `26`; metal avg `-0.0149` n `20`; unknown avg `-0.2376` n `1136`
- 1h: commodity avg `0.1136` n `13`; crypto_alt avg `0.2698` n `236`; crypto_major avg `0.0238` n `8`; equity avg `0.2991` n `151`; fx avg `0.0051` n `6`; index avg `0.0275` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.5424` n `1124`
- 4h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.119` n `236`; crypto_major avg `-0.1608` n `8`; equity avg `0.8358` n `151`; fx avg `0.0293` n `6`; index avg `0.1111` n `26`; metal avg `0.2723` n `20`; unknown avg `-0.0632` n `1124`
- 24h: commodity avg `-0.0024` n `13`; crypto_alt avg `2.7714` n `236`; crypto_major avg `1.0499` n `8`; equity avg `2.2536` n `151`; fx avg `0.0484` n `6`; index avg `0.3444` n `26`; metal avg `0.5041` n `20`; unknown avg `25.3313` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0705`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0628`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
