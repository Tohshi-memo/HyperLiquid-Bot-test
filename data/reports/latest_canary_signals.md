# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T07:52:27.012920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0663` n `13`; crypto_alt avg `0.3636` n `234`; crypto_major avg `0.1608` n `8`; equity avg `0.119` n `142`; fx avg `0.0012` n `6`; index avg `0.0224` n `26`; metal avg `0.0244` n `20`; unknown avg `8.1155` n `985`
- 1h: commodity avg `-0.1542` n `13`; crypto_alt avg `0.1598` n `234`; crypto_major avg `-0.0894` n `8`; equity avg `0.2591` n `142`; fx avg `-0.0591` n `6`; index avg `0.0642` n `26`; metal avg `0.0615` n `20`; unknown avg `8.1427` n `983`
- 4h: commodity avg `-0.3041` n `13`; crypto_alt avg `1.183` n `234`; crypto_major avg `0.8129` n `8`; equity avg `0.2848` n `142`; fx avg `-0.1315` n `6`; index avg `0.075` n `26`; metal avg `0.1048` n `20`; unknown avg `11.2551` n `947`
- 24h: commodity avg `-0.3908` n `13`; crypto_alt avg `1.2579` n `234`; crypto_major avg `1.8477` n `8`; equity avg `0.8532` n `142`; fx avg `-0.328` n `6`; index avg `0.1992` n `26`; metal avg `0.1543` n `20`; unknown avg `1144.5655` n `841`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
