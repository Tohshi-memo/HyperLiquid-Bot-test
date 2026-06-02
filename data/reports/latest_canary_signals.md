# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T04:22:19.224124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.1372` n `228`; crypto_major avg `-0.1416` n `8`; equity avg `-0.0895` n `69`; fx avg `0.0211` n `6`; index avg `0.0812` n `23`; metal avg `0.0568` n `18`; unknown avg `0.9391` n `422`
- 1h: commodity avg `-0.2056` n `12`; crypto_alt avg `0.1169` n `228`; crypto_major avg `-0.2624` n `8`; equity avg `0.378` n `69`; fx avg `0.0287` n `6`; index avg `0.1158` n `23`; metal avg `0.3269` n `18`; unknown avg `2.1035` n `422`
- 4h: commodity avg `-0.2742` n `12`; crypto_alt avg `0.0696` n `228`; crypto_major avg `-0.1663` n `8`; equity avg `0.5271` n `69`; fx avg `0.0675` n `6`; index avg `-0.1987` n `23`; metal avg `0.3587` n `18`; unknown avg `-0.2` n `422`
- 24h: commodity avg `-0.7464` n `12`; crypto_alt avg `-0.4713` n `228`; crypto_major avg `-0.8946` n `8`; equity avg `-0.4458` n `69`; fx avg `0.0661` n `6`; index avg `-0.8051` n `23`; metal avg `0.1631` n `18`; unknown avg `3.0375` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
