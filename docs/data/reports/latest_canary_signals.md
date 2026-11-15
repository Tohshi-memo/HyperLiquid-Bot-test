# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T15:22:27.592676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.016` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0235` n `13`; crypto_alt avg `0.2312` n `239`; crypto_major avg `0.2297` n `8`; equity avg `0.0695` n `162`; fx avg `-0.0013` n `6`; index avg `0.0077` n `27`; metal avg `0.022` n `20`; unknown avg `4.7375` n `1262`
- 1h: commodity avg `0.0415` n `13`; crypto_alt avg `-0.5523` n `239`; crypto_major avg `-0.7892` n `8`; equity avg `-0.1883` n `162`; fx avg `-0.001` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0421` n `20`; unknown avg `357.308` n `1262`
- 4h: commodity avg `-0.0392` n `13`; crypto_alt avg `-0.9131` n `239`; crypto_major avg `-1.0271` n `8`; equity avg `-0.3135` n `162`; fx avg `-0.0199` n `6`; index avg `-0.0111` n `27`; metal avg `-0.034` n `20`; unknown avg `159.8292` n `1253`
- 24h: commodity avg `0.0284` n `13`; crypto_alt avg `-2.1953` n `239`; crypto_major avg `-1.6476` n `8`; equity avg `-0.4372` n `162`; fx avg `-0.0081` n `6`; index avg `-0.0225` n `27`; metal avg `-0.2601` n `20`; unknown avg `0.1947` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
