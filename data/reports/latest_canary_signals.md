# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T10:22:17.330382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.1061` n `228`; crypto_major avg `-0.088` n `8`; equity avg `-0.0558` n `67`; fx avg `-0.0073` n `6`; index avg `-0.0256` n `23`; metal avg `0.0729` n `18`; unknown avg `0.9527` n `386`
- 1h: commodity avg `-0.1709` n `12`; crypto_alt avg `-0.5345` n `228`; crypto_major avg `-0.3426` n `8`; equity avg `-0.2234` n `67`; fx avg `-0.007` n `6`; index avg `-0.0774` n `23`; metal avg `0.6875` n `18`; unknown avg `0.9956` n `386`
- 4h: commodity avg `0.1048` n `12`; crypto_alt avg `-0.1583` n `228`; crypto_major avg `0.1174` n `8`; equity avg `-0.5874` n `67`; fx avg `-0.0315` n `6`; index avg `-0.1632` n `23`; metal avg `0.1932` n `18`; unknown avg `0.6555` n `386`
- 24h: commodity avg `0.0197` n `12`; crypto_alt avg `1.4421` n `228`; crypto_major avg `0.1352` n `8`; equity avg `0.688` n `67`; fx avg `0.0947` n `6`; index avg `0.491` n `23`; metal avg `0.6208` n `18`; unknown avg `1.9091` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0382`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0378`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0326`, n `668`, weak_sample_signal
