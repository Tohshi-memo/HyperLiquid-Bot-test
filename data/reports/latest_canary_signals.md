# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T14:52:27.598661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1687` n `13`; crypto_alt avg `0.0727` n `235`; crypto_major avg `0.0584` n `8`; equity avg `-0.1412` n `143`; fx avg `0.0115` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0471` n `20`; unknown avg `2.4192` n `982`
- 1h: commodity avg `-0.1741` n `13`; crypto_alt avg `-0.5536` n `235`; crypto_major avg `-0.7553` n `8`; equity avg `0.2463` n `143`; fx avg `0.0206` n `6`; index avg `0.0297` n `26`; metal avg `-0.1506` n `20`; unknown avg `1.3745` n `940`
- 4h: commodity avg `0.0143` n `13`; crypto_alt avg `0.2444` n `235`; crypto_major avg `-0.5975` n `8`; equity avg `0.7526` n `142`; fx avg `0.0439` n `6`; index avg `0.2136` n `26`; metal avg `-0.1312` n `20`; unknown avg `1.1544` n `934`
- 24h: commodity avg `-0.6164` n `13`; crypto_alt avg `3.4685` n `235`; crypto_major avg `2.0631` n `8`; equity avg `2.5348` n `142`; fx avg `-0.1557` n `6`; index avg `0.6163` n `26`; metal avg `0.0733` n `20`; unknown avg `104.2848` n `812`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
