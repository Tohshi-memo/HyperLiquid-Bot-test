# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T03:57:52.820290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `0.087` n `8`; equity avg `0.2855` n `114`; fx avg `0.0099` n `6`; index avg `0.0183` n `25`; metal avg `-0.0222` n `20`; unknown avg `-0.0476` n `793`
- 1h: commodity avg `0.0542` n `12`; crypto_alt avg `-0.2236` n `230`; crypto_major avg `0.058` n `8`; equity avg `0.1245` n `114`; fx avg `0.0322` n `6`; index avg `-0.0404` n `25`; metal avg `-0.0439` n `20`; unknown avg `-0.1997` n `793`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `-1.1828` n `230`; crypto_major avg `-0.6185` n `8`; equity avg `-1.4309` n `114`; fx avg `-0.0427` n `6`; index avg `-0.2645` n `25`; metal avg `-0.2568` n `20`; unknown avg `0.6845` n `793`
- 24h: commodity avg `0.6563` n `12`; crypto_alt avg `-1.4557` n `230`; crypto_major avg `-0.106` n `8`; equity avg `-0.9858` n `114`; fx avg `-0.0179` n `6`; index avg `-0.2868` n `25`; metal avg `-0.1988` n `20`; unknown avg `-0.0051` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
