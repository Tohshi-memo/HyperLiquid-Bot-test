# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T02:37:33.832694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.1553` n `228`; crypto_major avg `0.26` n `8`; equity avg `-0.043` n `88`; fx avg `0.0035` n `6`; index avg `-0.0132` n `25`; metal avg `0.0705` n `20`; unknown avg `-0.2068` n `763`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.1606` n `228`; crypto_major avg `0.1334` n `8`; equity avg `-0.0378` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0179` n `25`; metal avg `0.1044` n `20`; unknown avg `-0.3517` n `761`
- 4h: commodity avg `-0.0817` n `12`; crypto_alt avg `-0.0366` n `228`; crypto_major avg `-0.1743` n `8`; equity avg `-0.1009` n `88`; fx avg `-0.005` n `6`; index avg `0.0466` n `25`; metal avg `0.3` n `20`; unknown avg `21.3978` n `761`
- 24h: commodity avg `-0.6254` n `12`; crypto_alt avg `2.0295` n `228`; crypto_major avg `1.0973` n `8`; equity avg `-0.8866` n `88`; fx avg `-0.0223` n `6`; index avg `-0.2363` n `25`; metal avg `0.9454` n `20`; unknown avg `25.0527` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
