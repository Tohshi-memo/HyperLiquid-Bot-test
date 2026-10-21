# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T06:07:29.963972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `13`; crypto_alt avg `0.1102` n `237`; crypto_major avg `0.0804` n `8`; equity avg `0.067` n `151`; fx avg `-0.0225` n `6`; index avg `0.0304` n `26`; metal avg `-0.0304` n `20`; unknown avg `-0.0975` n `1180`
- 1h: commodity avg `0.0611` n `13`; crypto_alt avg `-0.2004` n `237`; crypto_major avg `-0.1454` n `8`; equity avg `0.0438` n `151`; fx avg `-0.0104` n `6`; index avg `0.0188` n `26`; metal avg `-0.0556` n `20`; unknown avg `-0.2065` n `1180`
- 4h: commodity avg `-0.0466` n `13`; crypto_alt avg `-0.3535` n `237`; crypto_major avg `-0.4081` n `8`; equity avg `-0.3871` n `151`; fx avg `-0.0729` n `6`; index avg `-0.0841` n `26`; metal avg `-0.1165` n `20`; unknown avg `0.497` n `1173`
- 24h: commodity avg `-0.1086` n `13`; crypto_alt avg `2.7837` n `237`; crypto_major avg `1.8874` n `8`; equity avg `2.8294` n `151`; fx avg `-0.0167` n `6`; index avg `0.3902` n `26`; metal avg `-0.0878` n `20`; unknown avg `5260.9893` n `992`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
