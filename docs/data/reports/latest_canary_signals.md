# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T16:58:53.612319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0489` n `230`; crypto_major avg `0.1348` n `8`; equity avg `-0.0` n `114`; fx avg `0.0029` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0018` n `20`; unknown avg `7.2872` n `791`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.0614` n `230`; crypto_major avg `0.0818` n `8`; equity avg `-0.0159` n `114`; fx avg `0.0023` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0089` n `20`; unknown avg `8.7641` n `791`
- 4h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.4712` n `230`; crypto_major avg `0.3588` n `8`; equity avg `0.0272` n `114`; fx avg `-0.0059` n `6`; index avg `0.0042` n `25`; metal avg `-0.0122` n `20`; unknown avg `10.2693` n `791`
- 24h: commodity avg `-0.1099` n `12`; crypto_alt avg `0.8427` n `230`; crypto_major avg `0.388` n `8`; equity avg `0.289` n `114`; fx avg `0.0267` n `6`; index avg `0.0435` n `25`; metal avg `-0.0258` n `20`; unknown avg `-0.0692` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
