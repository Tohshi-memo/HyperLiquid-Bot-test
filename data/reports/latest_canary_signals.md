# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T04:52:24.924602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.1709` n `233`; crypto_major avg `-0.1165` n `8`; equity avg `0.0481` n `134`; fx avg `0.0031` n `6`; index avg `0.0174` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.5641` n `797`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1149` n `233`; crypto_major avg `-0.0279` n `8`; equity avg `0.1649` n `134`; fx avg `0.0011` n `6`; index avg `0.039` n `26`; metal avg `0.0331` n `20`; unknown avg `1.3099` n `789`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `0.0983` n `233`; crypto_major avg `0.2782` n `8`; equity avg `0.1054` n `134`; fx avg `-0.0065` n `6`; index avg `0.0686` n `26`; metal avg `0.0267` n `20`; unknown avg `10.1616` n `789`
- 24h: commodity avg `0.044` n `12`; crypto_alt avg `-3.7382` n `233`; crypto_major avg `-2.5569` n `8`; equity avg `-1.0611` n `134`; fx avg `0.0091` n `6`; index avg `-0.1553` n `26`; metal avg `0.4149` n `20`; unknown avg `1.4066` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
