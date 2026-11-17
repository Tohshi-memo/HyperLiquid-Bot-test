# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T10:52:27.934972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0921` n `13`; crypto_alt avg `-0.0706` n `239`; crypto_major avg `-0.0756` n `8`; equity avg `-0.158` n `162`; fx avg `-0.0077` n `6`; index avg `-0.0219` n `27`; metal avg `0.018` n `20`; unknown avg `-0.0512` n `1266`
- 1h: commodity avg `0.0437` n `13`; crypto_alt avg `-0.1781` n `239`; crypto_major avg `-0.3257` n `8`; equity avg `-0.1808` n `162`; fx avg `-0.039` n `6`; index avg `0.0017` n `27`; metal avg `-0.0079` n `20`; unknown avg `316.2493` n `1264`
- 4h: commodity avg `0.2855` n `13`; crypto_alt avg `-0.6053` n `239`; crypto_major avg `-0.7692` n `8`; equity avg `-0.8189` n `162`; fx avg `-0.0689` n `6`; index avg `-0.0622` n `27`; metal avg `-0.1007` n `20`; unknown avg `208.3131` n `1198`
- 24h: commodity avg `-0.7355` n `13`; crypto_alt avg `0.36` n `239`; crypto_major avg `0.2614` n `8`; equity avg `-3.0787` n `162`; fx avg `-0.0677` n `6`; index avg `-0.2874` n `27`; metal avg `-0.1787` n `20`; unknown avg `11.4765` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
