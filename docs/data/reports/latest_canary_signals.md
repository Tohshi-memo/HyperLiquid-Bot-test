# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T00:22:19.259419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `0.2791` n `228`; crypto_major avg `0.172` n `8`; equity avg `0.0072` n `65`; fx avg `-0.0085` n `5`; index avg `-0.158` n `23`; metal avg `0.0089` n `18`; unknown avg `0.1215` n `375`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.2468` n `228`; crypto_major avg `0.1613` n `8`; equity avg `0.0007` n `65`; fx avg `-0.0096` n `5`; index avg `-0.0207` n `23`; metal avg `-0.0419` n `18`; unknown avg `-0.1665` n `375`
- 4h: commodity avg `-0.26` n `12`; crypto_alt avg `0.7866` n `228`; crypto_major avg `0.1652` n `8`; equity avg `0.253` n `65`; fx avg `-0.0406` n `5`; index avg `0.0477` n `23`; metal avg `-0.2151` n `18`; unknown avg `-0.256` n `375`
- 24h: commodity avg `-0.9004` n `12`; crypto_alt avg `3.5562` n `228`; crypto_major avg `1.5913` n `8`; equity avg `3.8725` n `65`; fx avg `0.1192` n `5`; index avg `1.4063` n `23`; metal avg `0.6833` n `18`; unknown avg `0.969` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
