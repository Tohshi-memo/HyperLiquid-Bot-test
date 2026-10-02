# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T10:22:28.101534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0628` n `13`; crypto_alt avg `-0.1704` n `234`; crypto_major avg `-0.046` n `8`; equity avg `-0.0727` n `142`; fx avg `-0.0185` n `6`; index avg `-0.017` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.2742` n `983`
- 1h: commodity avg `0.0562` n `13`; crypto_alt avg `-0.1719` n `234`; crypto_major avg `-0.0188` n `8`; equity avg `-0.1748` n `142`; fx avg `-0.003` n `6`; index avg `-0.0328` n `26`; metal avg `-0.1416` n `20`; unknown avg `0.405` n `981`
- 4h: commodity avg `-0.5032` n `13`; crypto_alt avg `0.3011` n `234`; crypto_major avg `0.3198` n `8`; equity avg `0.3601` n `142`; fx avg `-0.0594` n `6`; index avg `0.0844` n `26`; metal avg `-0.2137` n `20`; unknown avg `-0.4005` n `907`
- 24h: commodity avg `-0.5945` n `13`; crypto_alt avg `2.1491` n `234`; crypto_major avg `2.3521` n `8`; equity avg `1.0829` n `142`; fx avg `-0.3249` n `6`; index avg `0.1904` n `26`; metal avg `0.0197` n `20`; unknown avg `-0.1672` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
