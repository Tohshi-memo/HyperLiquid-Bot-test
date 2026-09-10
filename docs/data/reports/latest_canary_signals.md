# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T11:16:06.494241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.3339` n `233`; crypto_major avg `0.2684` n `8`; equity avg `0.0326` n `134`; fx avg `0.0033` n `6`; index avg `0.0048` n `26`; metal avg `-0.015` n `20`; unknown avg `1.034` n `797`
- 1h: commodity avg `0.0533` n `12`; crypto_alt avg `0.1727` n `233`; crypto_major avg `0.0466` n `8`; equity avg `-0.1559` n `134`; fx avg `0.0237` n `6`; index avg `-0.0533` n `26`; metal avg `-0.3376` n `20`; unknown avg `0.6806` n `795`
- 4h: commodity avg `0.2401` n `12`; crypto_alt avg `-0.2241` n `233`; crypto_major avg `-0.1079` n `8`; equity avg `-0.5018` n `134`; fx avg `0.0536` n `6`; index avg `-0.1167` n `26`; metal avg `-0.5809` n `20`; unknown avg `0.6744` n `789`
- 24h: commodity avg `-0.0302` n `12`; crypto_alt avg `-3.7011` n `233`; crypto_major avg `-2.4461` n `8`; equity avg `-0.9225` n `134`; fx avg `0.109` n `6`; index avg `-0.0493` n `26`; metal avg `-0.3741` n `20`; unknown avg `-0.6472` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
