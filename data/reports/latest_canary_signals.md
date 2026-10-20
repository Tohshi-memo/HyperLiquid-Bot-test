# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T00:22:35.978708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `13`; crypto_alt avg `-0.3104` n `237`; crypto_major avg `-0.3755` n `8`; equity avg `-0.3226` n `151`; fx avg `0.006` n `6`; index avg `-0.0742` n `26`; metal avg `-0.0756` n `20`; unknown avg `-0.1025` n `1198`
- 1h: commodity avg `0.0246` n `13`; crypto_alt avg `-0.4816` n `237`; crypto_major avg `-0.5748` n `8`; equity avg `-0.9411` n `151`; fx avg `-0.0256` n `6`; index avg `-0.1648` n `26`; metal avg `-0.0608` n `20`; unknown avg `0.1119` n `1190`
- 4h: commodity avg `-0.0188` n `13`; crypto_alt avg `-0.0697` n `237`; crypto_major avg `-0.2159` n `8`; equity avg `-0.7616` n `151`; fx avg `-0.0324` n `6`; index avg `-0.1377` n `26`; metal avg `-0.1056` n `20`; unknown avg `3.6238` n `1166`
- 24h: commodity avg `0.1574` n `13`; crypto_alt avg `0.1367` n `237`; crypto_major avg `-0.1967` n `8`; equity avg `-0.2298` n `151`; fx avg `-0.0617` n `6`; index avg `-0.0117` n `26`; metal avg `-0.2742` n `20`; unknown avg `5.0187` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
