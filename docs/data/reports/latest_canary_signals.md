# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T18:22:32.740941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3892` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.5146` n `234`; crypto_major avg `0.3174` n `8`; equity avg `-0.0011` n `142`; fx avg `0.0017` n `6`; index avg `0.0246` n `26`; metal avg `0.0526` n `20`; unknown avg `1.8356` n `962`
- 1h: commodity avg `-0.2057` n `12`; crypto_alt avg `0.8108` n `234`; crypto_major avg `0.5696` n `8`; equity avg `0.1331` n `142`; fx avg `0.0099` n `6`; index avg `0.0658` n `26`; metal avg `0.1696` n `20`; unknown avg `3.6213` n `960`
- 4h: commodity avg `-0.2705` n `12`; crypto_alt avg `-1.5738` n `234`; crypto_major avg `-1.4267` n `8`; equity avg `-0.545` n `142`; fx avg `-0.0222` n `6`; index avg `-0.0375` n `26`; metal avg `0.0166` n `20`; unknown avg `8.4297` n `892`
- 24h: commodity avg `-0.6277` n `12`; crypto_alt avg `-0.2517` n `234`; crypto_major avg `-1.1485` n `8`; equity avg `0.2619` n `142`; fx avg `-0.1702` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0391` n `20`; unknown avg `3.3373` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
