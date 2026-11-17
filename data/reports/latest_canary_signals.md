# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T18:22:26.820147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3169` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0461` n `13`; crypto_alt avg `-0.0211` n `239`; crypto_major avg `0.0894` n `8`; equity avg `0.0305` n `163`; fx avg `0.0074` n `6`; index avg `-0.0046` n `27`; metal avg `0.0051` n `20`; unknown avg `-0.2081` n `1263`
- 1h: commodity avg `0.1292` n `13`; crypto_alt avg `-0.4461` n `239`; crypto_major avg `-0.1192` n `8`; equity avg `-0.3792` n `163`; fx avg `0.0066` n `6`; index avg `-0.0489` n `27`; metal avg `-0.0689` n `20`; unknown avg `-0.3381` n `1263`
- 4h: commodity avg `0.0706` n `13`; crypto_alt avg `-1.6918` n `239`; crypto_major avg `-1.4824` n `8`; equity avg `-1.9269` n `163`; fx avg `0.046` n `6`; index avg `-0.1655` n `27`; metal avg `-0.0681` n `20`; unknown avg `0.0724` n `1245`
- 24h: commodity avg `0.1494` n `13`; crypto_alt avg `-0.7178` n `239`; crypto_major avg `-0.1801` n `8`; equity avg `-1.8054` n `163`; fx avg `0.0557` n `6`; index avg `-0.2312` n `27`; metal avg `0.0781` n `20`; unknown avg `8.0488` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
