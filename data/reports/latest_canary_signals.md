# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T18:07:44.161392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3424` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0521` n `13`; crypto_alt avg `-0.2476` n `239`; crypto_major avg `-0.2273` n `8`; equity avg `-0.0358` n `163`; fx avg `0.0037` n `6`; index avg `0.0059` n `27`; metal avg `-0.0062` n `20`; unknown avg `-0.1633` n `1259`
- 1h: commodity avg `0.0778` n `13`; crypto_alt avg `-0.3008` n `239`; crypto_major avg `-0.0855` n `8`; equity avg `-0.0995` n `163`; fx avg `0.0045` n `6`; index avg `0.0048` n `27`; metal avg `-0.0226` n `20`; unknown avg `19.3561` n `1261`
- 4h: commodity avg `0.0914` n `13`; crypto_alt avg `-1.7202` n `239`; crypto_major avg `-1.5151` n `8`; equity avg `-2.0312` n `163`; fx avg `0.0461` n `6`; index avg `-0.1727` n `27`; metal avg `-0.0538` n `20`; unknown avg `0.3824` n `1245`
- 24h: commodity avg `0.1275` n `13`; crypto_alt avg `-0.5429` n `239`; crypto_major avg `-0.1599` n `8`; equity avg `-1.9931` n `163`; fx avg `0.0361` n `6`; index avg `-0.2374` n `27`; metal avg `0.0365` n `20`; unknown avg `13.7178` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
