# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T01:37:30.698668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.2263` n `234`; crypto_major avg `0.1581` n `8`; equity avg `-0.1789` n `142`; fx avg `-0.026` n `6`; index avg `-0.0259` n `26`; metal avg `-0.0151` n `20`; unknown avg `0.2008` n `985`
- 1h: commodity avg `-0.1166` n `13`; crypto_alt avg `-0.292` n `234`; crypto_major avg `-0.1276` n `8`; equity avg `-0.3453` n `142`; fx avg `-0.0452` n `6`; index avg `-0.0586` n `26`; metal avg `-0.1468` n `20`; unknown avg `0.1974` n `983`
- 4h: commodity avg `-0.2264` n `13`; crypto_alt avg `0.3018` n `234`; crypto_major avg `0.254` n `8`; equity avg `-0.089` n `142`; fx avg `-0.0152` n `6`; index avg `-0.013` n `26`; metal avg `-0.2417` n `20`; unknown avg `0.189` n `937`
- 24h: commodity avg `0.3343` n `13`; crypto_alt avg `-0.5906` n `234`; crypto_major avg `-0.1775` n `8`; equity avg `0.625` n `142`; fx avg `-0.235` n `6`; index avg `0.0774` n `26`; metal avg `-0.2712` n `20`; unknown avg `-0.0569` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
