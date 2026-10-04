# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T19:07:42.156738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `0.0681` n `235`; crypto_major avg `0.0432` n `8`; equity avg `-0.0099` n `144`; fx avg `0.0007` n `6`; index avg `-0.0039` n `26`; metal avg `0.0022` n `20`; unknown avg `1.4162` n `1076`
- 1h: commodity avg `0.0343` n `13`; crypto_alt avg `0.2893` n `235`; crypto_major avg `0.0551` n `8`; equity avg `-0.0327` n `144`; fx avg `0.0014` n `6`; index avg `-0.0056` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.0633` n `1074`
- 4h: commodity avg `0.0212` n `13`; crypto_alt avg `0.0788` n `235`; crypto_major avg `0.2374` n `8`; equity avg `-0.0125` n `144`; fx avg `0.0001` n `6`; index avg `-0.0092` n `26`; metal avg `-0.002` n `20`; unknown avg `1.3382` n `1068`
- 24h: commodity avg `0.0382` n `13`; crypto_alt avg `1.264` n `235`; crypto_major avg `0.9754` n `8`; equity avg `0.1966` n `144`; fx avg `0.0292` n `6`; index avg `-0.0181` n `26`; metal avg `0.0099` n `20`; unknown avg `0.9895` n `1017`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
