# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T02:22:27.733635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.2836` n `234`; crypto_major avg `0.1477` n `8`; equity avg `0.0521` n `140`; fx avg `-0.002` n `6`; index avg `-0.008` n `26`; metal avg `-0.0008` n `20`; unknown avg `3.4034` n `942`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.8683` n `234`; crypto_major avg `0.6018` n `8`; equity avg `0.0032` n `140`; fx avg `0.0002` n `6`; index avg `-0.0206` n `26`; metal avg `0.0129` n `20`; unknown avg `2.3646` n `940`
- 4h: commodity avg `0.1928` n `12`; crypto_alt avg `0.489` n `234`; crypto_major avg `0.3307` n `8`; equity avg `-0.131` n `140`; fx avg `-0.007` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0378` n `20`; unknown avg `0.3107` n `934`
- 24h: commodity avg `0.1203` n `12`; crypto_alt avg `5.7899` n `234`; crypto_major avg `6.3015` n `8`; equity avg `1.3286` n `140`; fx avg `0.142` n `6`; index avg `0.1187` n `26`; metal avg `0.1894` n `20`; unknown avg `4.2608` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
