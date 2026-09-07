# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T22:22:30.665459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.1536` n `232`; crypto_major avg `-0.087` n `8`; equity avg `-0.0481` n `134`; fx avg `-0.0069` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0013` n `20`; unknown avg `15.837` n `797`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.4787` n `232`; crypto_major avg `-0.2421` n `8`; equity avg `-0.1047` n `134`; fx avg `0.0037` n `6`; index avg `-0.0189` n `26`; metal avg `0.0037` n `20`; unknown avg `7.0841` n `794`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `0.2088` n `232`; crypto_major avg `-0.0444` n `8`; equity avg `-0.0161` n `134`; fx avg `-0.0011` n `6`; index avg `0.0005` n `26`; metal avg `0.053` n `20`; unknown avg `7.3337` n `752`
- 24h: commodity avg `0.1855` n `12`; crypto_alt avg `0.2441` n `232`; crypto_major avg `-0.8292` n `8`; equity avg `0.4425` n `134`; fx avg `-0.1618` n `6`; index avg `0.0723` n `26`; metal avg `0.0818` n `20`; unknown avg `7801.385` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
