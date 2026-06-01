# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T00:52:17.884236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.098` n `12`; crypto_alt avg `0.1449` n `228`; crypto_major avg `0.2552` n `8`; equity avg `0.0412` n `69`; fx avg `0.0096` n `6`; index avg `0.0107` n `23`; metal avg `0.0775` n `18`; unknown avg `0.0581` n `421`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `0.8976` n `228`; crypto_major avg `0.7111` n `8`; equity avg `0.034` n `69`; fx avg `0.0536` n `6`; index avg `0.2964` n `23`; metal avg `0.0039` n `18`; unknown avg `0.0957` n `421`
- 4h: commodity avg `0.4701` n `12`; crypto_alt avg `1.9216` n `228`; crypto_major avg `1.3045` n `8`; equity avg `0.0776` n `69`; fx avg `0.0407` n `6`; index avg `0.0478` n `23`; metal avg `0.4124` n `18`; unknown avg `0.8385` n `421`
- 24h: commodity avg `0.8981` n `12`; crypto_alt avg `1.4981` n `228`; crypto_major avg `0.8114` n `8`; equity avg `0.6489` n `69`; fx avg `0.035` n `6`; index avg `0.4564` n `23`; metal avg `0.2863` n `18`; unknown avg `2.2062` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2884`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2533`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
