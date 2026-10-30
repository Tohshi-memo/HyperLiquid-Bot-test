# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T11:52:37.480056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `13`; crypto_alt avg `-0.2027` n `238`; crypto_major avg `-0.2578` n `8`; equity avg `-0.1641` n `156`; fx avg `-0.0037` n `6`; index avg `-0.0261` n `27`; metal avg `-0.1213` n `20`; unknown avg `-0.2573` n `1261`
- 1h: commodity avg `-0.0567` n `13`; crypto_alt avg `-0.0476` n `238`; crypto_major avg `-0.3706` n `8`; equity avg `-0.3667` n `156`; fx avg `-0.0611` n `6`; index avg `-0.0318` n `27`; metal avg `-0.109` n `20`; unknown avg `-0.0945` n `1255`
- 4h: commodity avg `0.0233` n `13`; crypto_alt avg `0.6553` n `238`; crypto_major avg `-0.1359` n `8`; equity avg `-1.0615` n `156`; fx avg `-0.0211` n `6`; index avg `-0.1154` n `27`; metal avg `-0.1056` n `20`; unknown avg `22.8243` n `1190`
- 24h: commodity avg `0.1604` n `13`; crypto_alt avg `-3.7862` n `238`; crypto_major avg `-2.3988` n `8`; equity avg `-4.0742` n `156`; fx avg `0.0409` n `6`; index avg `-0.4416` n `27`; metal avg `-0.7114` n `20`; unknown avg `23.5712` n `1034`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
