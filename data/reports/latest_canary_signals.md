# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T10:52:18.398953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0803` n `12`; crypto_alt avg `-0.1141` n `228`; crypto_major avg `-0.0752` n `8`; equity avg `0.0916` n `67`; fx avg `-0.0068` n `6`; index avg `-0.0219` n `23`; metal avg `-0.0639` n `18`; unknown avg `0.0264` n `386`
- 1h: commodity avg `-0.1298` n `12`; crypto_alt avg `-0.1225` n `228`; crypto_major avg `-0.0536` n `8`; equity avg `-0.2519` n `67`; fx avg `-0.0206` n `6`; index avg `-0.181` n `23`; metal avg `-0.1702` n `18`; unknown avg `-0.0685` n `386`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.0804` n `228`; crypto_major avg `0.3802` n `8`; equity avg `-0.6475` n `67`; fx avg `-0.0247` n `6`; index avg `-0.2702` n `23`; metal avg `-0.0448` n `18`; unknown avg `-0.1423` n `386`
- 24h: commodity avg `-1.2453` n `12`; crypto_alt avg `2.4598` n `228`; crypto_major avg `0.8149` n `8`; equity avg `1.3581` n `67`; fx avg `0.0718` n `6`; index avg `0.85` n `23`; metal avg `1.0236` n `18`; unknown avg `1.2217` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0378`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0377`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0319`, n `668`, weak_sample_signal
