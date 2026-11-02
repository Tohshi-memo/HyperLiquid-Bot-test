# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T18:37:31.687638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4297` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.0817` n `239`; crypto_major avg `-0.0742` n `8`; equity avg `-0.1984` n `156`; fx avg `-0.0078` n `6`; index avg `-0.0194` n `27`; metal avg `-0.0457` n `20`; unknown avg `12.5456` n `1265`
- 1h: commodity avg `-0.0596` n `13`; crypto_alt avg `-0.238` n `239`; crypto_major avg `-0.206` n `8`; equity avg `-0.4937` n `156`; fx avg `-0.0244` n `6`; index avg `-0.0455` n `27`; metal avg `-0.0173` n `20`; unknown avg `0.101` n `1239`
- 4h: commodity avg `-0.5458` n `13`; crypto_alt avg `-1.6023` n `239`; crypto_major avg `-1.4621` n `8`; equity avg `-0.9174` n `156`; fx avg `-0.0083` n `6`; index avg `-0.0324` n `27`; metal avg `-0.0064` n `20`; unknown avg `15.641` n `1229`
- 24h: commodity avg `-1.3501` n `13`; crypto_alt avg `-2.9095` n `238`; crypto_major avg `-1.7151` n `8`; equity avg `-1.6695` n `156`; fx avg `0.2412` n `6`; index avg `0.1537` n `27`; metal avg `0.2942` n `20`; unknown avg `8.3206` n `1055`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
