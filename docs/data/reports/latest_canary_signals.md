# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T22:07:26.674349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1572` n `12`; crypto_alt avg `-0.0946` n `228`; crypto_major avg `-0.0908` n `8`; equity avg `0.0845` n `74`; fx avg `0.0597` n `6`; index avg `0.0271` n `23`; metal avg `0.015` n `18`; unknown avg `-0.1054` n `547`
- 1h: commodity avg `0.2338` n `12`; crypto_alt avg `-0.8929` n `228`; crypto_major avg `-0.904` n `8`; equity avg `-0.3278` n `74`; fx avg `0.0135` n `6`; index avg `-0.0456` n `23`; metal avg `-0.1399` n `18`; unknown avg `-0.2569` n `547`
- 4h: commodity avg `0.307` n `12`; crypto_alt avg `0.1` n `228`; crypto_major avg `-0.2811` n `8`; equity avg `0.5747` n `74`; fx avg `-0.0653` n `6`; index avg `1.0378` n `23`; metal avg `0.0328` n `18`; unknown avg `0.0364` n `547`
- 24h: commodity avg `-0.5375` n `12`; crypto_alt avg `-2.2613` n `228`; crypto_major avg `-3.3711` n `8`; equity avg `-1.9761` n `74`; fx avg `0.1028` n `6`; index avg `-0.9274` n `23`; metal avg `-1.4931` n `18`; unknown avg `-1.2765` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0412`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
