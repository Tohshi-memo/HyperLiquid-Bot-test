# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T02:22:29.088991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.82` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.5277` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1234` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0289` n `13`; crypto_alt avg `-0.4194` n `239`; crypto_major avg `-0.3141` n `8`; equity avg `-0.525` n `158`; fx avg `0.0148` n `6`; index avg `-0.0818` n `27`; metal avg `-0.0465` n `20`; unknown avg `3.953` n `1264`
- 1h: commodity avg `-0.2708` n `13`; crypto_alt avg `-0.1548` n `239`; crypto_major avg `-0.2223` n `8`; equity avg `-0.3941` n `158`; fx avg `-0.0673` n `6`; index avg `-0.1137` n `27`; metal avg `-0.2193` n `20`; unknown avg `-0.2389` n `1258`
- 4h: commodity avg `-0.4144` n `13`; crypto_alt avg `-1.4` n `239`; crypto_major avg `-1.6108` n `8`; equity avg `-2.6407` n `158`; fx avg `-0.034` n `6`; index avg `-0.4874` n `27`; metal avg `-0.0831` n `20`; unknown avg `146.8042` n `1196`
- 24h: commodity avg `-0.1068` n `13`; crypto_alt avg `0.132` n `239`; crypto_major avg `-0.3839` n `8`; equity avg `-0.7116` n `158`; fx avg `0.1162` n `6`; index avg `-0.3054` n `27`; metal avg `-0.4902` n `20`; unknown avg `0.2358` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
