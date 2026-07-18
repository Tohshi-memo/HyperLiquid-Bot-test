# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T19:07:26.150350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `0.0523` n `230`; crypto_major avg `0.0564` n `8`; equity avg `0.0067` n `96`; fx avg `0.0003` n `6`; index avg `0.0026` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0679` n `770`
- 1h: commodity avg `0.1486` n `12`; crypto_alt avg `-0.0965` n `230`; crypto_major avg `0.0718` n `8`; equity avg `0.0138` n `96`; fx avg `-0.0286` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.103` n `770`
- 4h: commodity avg `0.2721` n `12`; crypto_alt avg `0.165` n `230`; crypto_major avg `0.4296` n `8`; equity avg `-0.0456` n `96`; fx avg `-0.0775` n `6`; index avg `-0.0377` n `25`; metal avg `-0.0427` n `20`; unknown avg `-0.0704` n `770`
- 24h: commodity avg `0.564` n `12`; crypto_alt avg `-0.9091` n `230`; crypto_major avg `0.1826` n `8`; equity avg `-0.6851` n `96`; fx avg `-0.1384` n `6`; index avg `-0.0416` n `25`; metal avg `0.0288` n `20`; unknown avg `-0.1978` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
