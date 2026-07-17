# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T10:52:26.931778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0371` n `230`; crypto_major avg `-0.0412` n `8`; equity avg `0.0344` n `96`; fx avg `-0.0164` n `6`; index avg `0.0083` n `25`; metal avg `-0.0519` n `20`; unknown avg `-0.0423` n `769`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.0187` n `230`; crypto_major avg `0.037` n `8`; equity avg `0.6764` n `96`; fx avg `-0.0376` n `6`; index avg `0.1231` n `25`; metal avg `-0.1` n `20`; unknown avg `-0.0104` n `769`
- 4h: commodity avg `0.3234` n `12`; crypto_alt avg `0.115` n `230`; crypto_major avg `0.3409` n `8`; equity avg `0.8045` n `96`; fx avg `-0.0271` n `6`; index avg `0.1151` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.0914` n `768`
- 24h: commodity avg `0.0143` n `12`; crypto_alt avg `-1.3942` n `230`; crypto_major avg `-2.5486` n `8`; equity avg `-4.2657` n `94`; fx avg `-0.0414` n `6`; index avg `-0.5716` n `25`; metal avg `-0.7484` n `20`; unknown avg `-0.3837` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
