# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T06:07:34.016448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5687` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `0.5051` n `233`; crypto_major avg `0.5258` n `8`; equity avg `0.1477` n `136`; fx avg `-0.0222` n `6`; index avg `0.0307` n `27`; metal avg `0.0523` n `20`; unknown avg `1.2673` n `866`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `0.3577` n `233`; crypto_major avg `0.4226` n `8`; equity avg `-0.0632` n `136`; fx avg `-0.0009` n `6`; index avg `0.0129` n `27`; metal avg `-0.0027` n `20`; unknown avg `0.2585` n `866`
- 4h: commodity avg `-0.0089` n `12`; crypto_alt avg `0.9683` n `233`; crypto_major avg `1.3914` n `8`; equity avg `-0.1773` n `136`; fx avg `-0.0309` n `6`; index avg `-0.0483` n `27`; metal avg `-0.0932` n `20`; unknown avg `8.2892` n `854`
- 24h: commodity avg `0.5108` n `12`; crypto_alt avg `-0.2988` n `233`; crypto_major avg `0.3984` n `8`; equity avg `-1.2963` n `136`; fx avg `0.0304` n `6`; index avg `-0.2902` n `26`; metal avg `-0.1335` n `20`; unknown avg `1.5` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
