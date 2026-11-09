# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T07:52:26.009178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5778` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5194` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `-0.3442` n `239`; crypto_major avg `-0.2959` n `8`; equity avg `-0.3789` n `158`; fx avg `0.0128` n `6`; index avg `-0.0392` n `27`; metal avg `-0.0573` n `20`; unknown avg `-0.009` n `1249`
- 1h: commodity avg `0.0037` n `13`; crypto_alt avg `-1.0964` n `239`; crypto_major avg `-0.8189` n `8`; equity avg `-1.015` n `158`; fx avg `0.0137` n `6`; index avg `-0.1282` n `27`; metal avg `-0.2026` n `20`; unknown avg `-0.1249` n `1235`
- 4h: commodity avg `-0.3883` n `13`; crypto_alt avg `-1.8976` n `239`; crypto_major avg `-1.8841` n `8`; equity avg `-2.2412` n `158`; fx avg `-0.0653` n `6`; index avg `-0.3063` n `27`; metal avg `-0.3647` n `20`; unknown avg `1.1165` n `1197`
- 24h: commodity avg `-0.2739` n `13`; crypto_alt avg `-3.5932` n `239`; crypto_major avg `-4.2207` n `8`; equity avg `-1.6643` n `158`; fx avg `-0.1517` n `6`; index avg `-0.2282` n `27`; metal avg `0.1174` n `20`; unknown avg `1.0909` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
