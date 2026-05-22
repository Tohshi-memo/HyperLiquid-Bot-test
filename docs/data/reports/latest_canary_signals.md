# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T09:52:16.694352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1882` n `12`; crypto_alt avg `0.0319` n `228`; crypto_major avg `-0.0004` n `8`; equity avg `0.1004` n `67`; fx avg `0.0023` n `6`; index avg `0.0626` n `23`; metal avg `0.1878` n `18`; unknown avg `0.0492` n `386`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0102` n `228`; crypto_major avg `-0.05` n `8`; equity avg `-0.2329` n `67`; fx avg `-0.0098` n `6`; index avg `-0.1489` n `23`; metal avg `0.3513` n `18`; unknown avg `-0.0496` n `386`
- 4h: commodity avg `0.3013` n `12`; crypto_alt avg `-0.302` n `228`; crypto_major avg `-0.0114` n `8`; equity avg `-0.4901` n `67`; fx avg `-0.0251` n `6`; index avg `-0.1779` n `23`; metal avg `-0.259` n `18`; unknown avg `-0.5818` n `376`
- 24h: commodity avg `0.2597` n `12`; crypto_alt avg `1.7399` n `228`; crypto_major avg `0.1866` n `8`; equity avg `0.8562` n `67`; fx avg `0.091` n `6`; index avg `0.543` n `23`; metal avg `0.5246` n `18`; unknown avg `1.0408` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.042`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0367`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0348`, n `668`, weak_sample_signal
