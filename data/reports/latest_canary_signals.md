# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T01:22:27.827423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `13`; crypto_alt avg `-0.0496` n `235`; crypto_major avg `0.0284` n `8`; equity avg `-0.0028` n `143`; fx avg `-0.0064` n `6`; index avg `0.0067` n `26`; metal avg `-0.0169` n `20`; unknown avg `0.0759` n `984`
- 1h: commodity avg `-0.0912` n `13`; crypto_alt avg `0.0634` n `235`; crypto_major avg `0.08` n `8`; equity avg `-0.0342` n `143`; fx avg `0.008` n `6`; index avg `0.0057` n `26`; metal avg `-0.0262` n `20`; unknown avg `0.4434` n `982`
- 4h: commodity avg `-0.0457` n `13`; crypto_alt avg `1.6076` n `235`; crypto_major avg `1.0043` n `8`; equity avg `0.0465` n `143`; fx avg `-0.0593` n `6`; index avg `0.017` n `26`; metal avg `-0.0205` n `20`; unknown avg `1.0759` n `960`
- 24h: commodity avg `0.144` n `13`; crypto_alt avg `0.3214` n `235`; crypto_major avg `0.271` n `8`; equity avg `0.7595` n `142`; fx avg `-0.172` n `6`; index avg `0.3077` n `26`; metal avg `-0.0441` n `20`; unknown avg `-0.357` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
