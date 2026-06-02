# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T02:06:20.879451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1023` n `12`; crypto_alt avg `-0.6984` n `228`; crypto_major avg `-0.5681` n `8`; equity avg `-0.084` n `69`; fx avg `-0.0195` n `6`; index avg `-0.0347` n `23`; metal avg `0.2017` n `18`; unknown avg `0.8353` n `422`
- 1h: commodity avg `-0.0634` n `12`; crypto_alt avg `-1.2383` n `228`; crypto_major avg `-1.087` n `8`; equity avg `-0.2378` n `69`; fx avg `0.0445` n `6`; index avg `-0.2147` n `23`; metal avg `-0.2552` n `18`; unknown avg `1.1734` n `422`
- 4h: commodity avg `-0.408` n `12`; crypto_alt avg `-0.9621` n `228`; crypto_major avg `-0.557` n `8`; equity avg `-0.9662` n `69`; fx avg `0.0422` n `6`; index avg `-0.5609` n `23`; metal avg `-0.0457` n `18`; unknown avg `1.4101` n `422`
- 24h: commodity avg `-0.5502` n `12`; crypto_alt avg `-1.5808` n `228`; crypto_major avg `-1.8342` n `8`; equity avg `-1.1942` n `69`; fx avg `0.014` n `6`; index avg `-0.5586` n `23`; metal avg `-0.6946` n `18`; unknown avg `1.9407` n `406`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
