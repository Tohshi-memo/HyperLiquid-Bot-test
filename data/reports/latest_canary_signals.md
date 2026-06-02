# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T15:22:32.597176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.26` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.5487` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.3099` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.8979` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6236` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2525` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.5521` n `228`; crypto_major avg `-0.2984` n `8`; equity avg `0.2673` n `69`; fx avg `0.0009` n `6`; index avg `0.0535` n `23`; metal avg `0.0924` n `18`; unknown avg `-0.5424` n `422`
- 1h: commodity avg `-0.3422` n `12`; crypto_alt avg `-1.5017` n `228`; crypto_major avg `-1.1094` n `8`; equity avg `0.2842` n `69`; fx avg `0.0191` n `6`; index avg `0.1431` n `23`; metal avg `0.5142` n `18`; unknown avg `-1.0716` n `422`
- 4h: commodity avg `-0.0968` n `12`; crypto_alt avg `-2.4023` n `228`; crypto_major avg `-2.0794` n `8`; equity avg `0.2305` n `69`; fx avg `-0.0105` n `6`; index avg `0.4693` n `23`; metal avg `-0.1815` n `18`; unknown avg `-0.3689` n `422`
- 24h: commodity avg `-1.3489` n `12`; crypto_alt avg `-1.4995` n `228`; crypto_major avg `-2.4133` n `8`; equity avg `0.6913` n `69`; fx avg `0.1891` n `6`; index avg `0.7559` n `23`; metal avg `1.0668` n `18`; unknown avg `-0.4998` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
