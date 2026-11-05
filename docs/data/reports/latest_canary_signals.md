# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T14:22:43.238701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5797` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1494` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1824` n `13`; crypto_alt avg `-0.2068` n `239`; crypto_major avg `-0.2488` n `8`; equity avg `-0.1486` n `158`; fx avg `0.0157` n `6`; index avg `-0.0251` n `27`; metal avg `0.0783` n `20`; unknown avg `0.3494` n `1254`
- 1h: commodity avg `0.0742` n `13`; crypto_alt avg `-0.1923` n `239`; crypto_major avg `-0.3025` n `8`; equity avg `-0.3407` n `158`; fx avg `0.0155` n `6`; index avg `-0.0516` n `27`; metal avg `0.253` n `20`; unknown avg `-0.1676` n `1254`
- 4h: commodity avg `0.3873` n `13`; crypto_alt avg `-1.2255` n `239`; crypto_major avg `-1.2713` n `8`; equity avg `-1.3877` n `158`; fx avg `0.0425` n `6`; index avg `-0.1219` n `27`; metal avg `0.3084` n `20`; unknown avg `15.4369` n `1229`
- 24h: commodity avg `-0.4838` n `13`; crypto_alt avg `0.1307` n `239`; crypto_major avg `0.8159` n `8`; equity avg `-2.9586` n `158`; fx avg `-0.0067` n `6`; index avg `-0.3409` n `27`; metal avg `0.9641` n `20`; unknown avg `18.1659` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2307`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.2023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
