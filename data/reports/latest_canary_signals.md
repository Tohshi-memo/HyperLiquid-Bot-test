# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T20:08:06.200638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.084` n `12`; crypto_alt avg `0.3786` n `232`; crypto_major avg `0.2707` n `8`; equity avg `0.0285` n `133`; fx avg `-0.0185` n `6`; index avg `-0.0041` n `26`; metal avg `0.0031` n `20`; unknown avg `0.1548` n `778`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.1632` n `232`; crypto_major avg `0.0725` n `8`; equity avg `0.1195` n `133`; fx avg `-0.0271` n `6`; index avg `0.0108` n `26`; metal avg `0.0679` n `20`; unknown avg `0.2871` n `778`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.1294` n `232`; crypto_major avg `0.0506` n `8`; equity avg `0.727` n `133`; fx avg `-0.0339` n `6`; index avg `0.0221` n `26`; metal avg `0.0934` n `20`; unknown avg `-0.0752` n `778`
- 24h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.0648` n `232`; crypto_major avg `-0.1518` n `8`; equity avg `0.911` n `133`; fx avg `-0.3783` n `6`; index avg `0.1434` n `26`; metal avg `0.5117` n `20`; unknown avg `0.3292` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
