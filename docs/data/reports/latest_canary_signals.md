# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:56:34.453472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0474` n `12`; crypto_alt avg `0.3078` n `231`; crypto_major avg `0.2629` n `8`; equity avg `0.0208` n `122`; fx avg `-0.0062` n `6`; index avg `-0.0018` n `25`; metal avg `0.0379` n `20`; unknown avg `0.0516` n `795`
- 1h: commodity avg `0.1042` n `12`; crypto_alt avg `0.1727` n `231`; crypto_major avg `0.1607` n `8`; equity avg `-0.0329` n `122`; fx avg `-0.0217` n `6`; index avg `-0.028` n `25`; metal avg `-0.0356` n `20`; unknown avg `0.084` n `794`
- 4h: commodity avg `-0.3285` n `12`; crypto_alt avg `-0.6757` n `231`; crypto_major avg `-0.839` n `8`; equity avg `0.5274` n `122`; fx avg `-0.0111` n `6`; index avg `0.0864` n `25`; metal avg `-0.0811` n `20`; unknown avg `-0.1505` n `794`
- 24h: commodity avg `-0.6453` n `12`; crypto_alt avg `0.5845` n `231`; crypto_major avg `1.4614` n `8`; equity avg `0.791` n `122`; fx avg `0.0056` n `6`; index avg `0.1475` n `25`; metal avg `-0.189` n `20`; unknown avg `-0.0742` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
