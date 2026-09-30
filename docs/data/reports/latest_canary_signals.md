# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T03:07:31.195492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `-0.2898` n `234`; crypto_major avg `-0.1379` n `8`; equity avg `-0.0192` n `142`; fx avg `0.0122` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0206` n `20`; unknown avg `2.8164` n `961`
- 1h: commodity avg `0.0641` n `12`; crypto_alt avg `-0.6326` n `234`; crypto_major avg `-0.2763` n `8`; equity avg `-0.2347` n `142`; fx avg `-0.0112` n `6`; index avg `-0.0285` n `26`; metal avg `0.0391` n `20`; unknown avg `2.9481` n `961`
- 4h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.4853` n `234`; crypto_major avg `-0.2671` n `8`; equity avg `-0.2513` n `142`; fx avg `-0.034` n `6`; index avg `-0.0441` n `26`; metal avg `-0.0688` n `20`; unknown avg `4.1661` n `955`
- 24h: commodity avg `-0.9249` n `12`; crypto_alt avg `2.4002` n `234`; crypto_major avg `0.8099` n `8`; equity avg `1.0078` n `142`; fx avg `-0.1796` n `6`; index avg `0.1374` n `26`; metal avg `0.2058` n `20`; unknown avg `3232.2618` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
