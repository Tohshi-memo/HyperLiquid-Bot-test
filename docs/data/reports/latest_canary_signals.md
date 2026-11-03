# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T23:07:31.070390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `-0.0721` n `239`; crypto_major avg `-0.1412` n `8`; equity avg `0.0934` n `158`; fx avg `-0.0036` n `6`; index avg `0.0145` n `27`; metal avg `0.0278` n `20`; unknown avg `142.9043` n `1210`
- 1h: commodity avg `-0.0364` n `13`; crypto_alt avg `-0.0599` n `239`; crypto_major avg `-0.1518` n `8`; equity avg `0.1393` n `158`; fx avg `-0.0111` n `6`; index avg `0.0135` n `27`; metal avg `0.0171` n `20`; unknown avg `144.0325` n `1202`
- 4h: commodity avg `0.1706` n `13`; crypto_alt avg `0.2611` n `239`; crypto_major avg `0.1461` n `8`; equity avg `1.1622` n `158`; fx avg `-0.0332` n `6`; index avg `0.1117` n `27`; metal avg `0.0258` n `20`; unknown avg `20.3952` n `1157`
- 24h: commodity avg `0.363` n `13`; crypto_alt avg `1.21` n `239`; crypto_major avg `1.2502` n `8`; equity avg `2.5446` n `158`; fx avg `0.0776` n `6`; index avg `0.2778` n `27`; metal avg `-0.4664` n `20`; unknown avg `-0.2563` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
