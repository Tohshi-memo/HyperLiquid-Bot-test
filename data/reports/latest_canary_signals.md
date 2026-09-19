# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T23:37:26.715460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0885` n `234`; crypto_major avg `0.0784` n `8`; equity avg `-0.0043` n `140`; fx avg `-0.0007` n `6`; index avg `0.0004` n `26`; metal avg `0.0066` n `20`; unknown avg `0.4554` n `927`
- 1h: commodity avg `0.0333` n `12`; crypto_alt avg `0.4623` n `234`; crypto_major avg `0.3199` n `8`; equity avg `-0.0384` n `140`; fx avg `-0.0175` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.5062` n `925`
- 4h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.2893` n `234`; crypto_major avg `-0.4557` n `8`; equity avg `0.0127` n `140`; fx avg `-0.0461` n `6`; index avg `0.0013` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.3422` n `895`
- 24h: commodity avg `0.0316` n `12`; crypto_alt avg `1.0821` n `234`; crypto_major avg `0.1107` n `8`; equity avg `-0.0286` n `140`; fx avg `-0.087` n `6`; index avg `0.0101` n `26`; metal avg `-0.0197` n `20`; unknown avg `1.0895` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
