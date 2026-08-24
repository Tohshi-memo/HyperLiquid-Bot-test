# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T05:06:44.015393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.0187` n `231`; crypto_major avg `0.1334` n `8`; equity avg `0.0382` n `122`; fx avg `0.0004` n `6`; index avg `0.0135` n `25`; metal avg `0.0317` n `20`; unknown avg `-0.1068` n `793`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `0.1135` n `231`; crypto_major avg `-0.0381` n `8`; equity avg `0.0834` n `122`; fx avg `-0.0174` n `6`; index avg `0.0262` n `25`; metal avg `0.0377` n `20`; unknown avg `0.355` n `793`
- 4h: commodity avg `0.0635` n `12`; crypto_alt avg `-1.0299` n `231`; crypto_major avg `-0.9827` n `8`; equity avg `-1.3785` n `122`; fx avg `-0.0305` n `6`; index avg `-0.1327` n `25`; metal avg `0.0272` n `20`; unknown avg `0.2184` n `793`
- 24h: commodity avg `-0.2921` n `12`; crypto_alt avg `4.2963` n `231`; crypto_major avg `1.4803` n `8`; equity avg `-0.982` n `122`; fx avg `-0.2036` n `6`; index avg `-0.0785` n `25`; metal avg `0.1523` n `20`; unknown avg `5.9792` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
