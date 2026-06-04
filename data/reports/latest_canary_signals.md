# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T19:07:23.113453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3699` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `-0.4153` n `228`; crypto_major avg `-0.4822` n `8`; equity avg `-0.1987` n `74`; fx avg `-0.0049` n `6`; index avg `-0.014` n `23`; metal avg `-0.0024` n `18`; unknown avg `-0.1038` n `424`
- 1h: commodity avg `0.3484` n `12`; crypto_alt avg `0.5727` n `228`; crypto_major avg `0.5095` n `8`; equity avg `-0.1986` n `74`; fx avg `-0.0041` n `6`; index avg `-0.0063` n `23`; metal avg `0.0224` n `18`; unknown avg `0.0693` n `424`
- 4h: commodity avg `0.1333` n `12`; crypto_alt avg `-0.4769` n `228`; crypto_major avg `-0.9349` n `8`; equity avg `-0.0153` n `74`; fx avg `-0.0431` n `6`; index avg `0.435` n `23`; metal avg `0.2747` n `18`; unknown avg `1.1787` n `424`
- 24h: commodity avg `-0.5494` n `12`; crypto_alt avg `-5.6279` n `228`; crypto_major avg `-4.0501` n `8`; equity avg `-1.0469` n `73`; fx avg `0.0488` n `6`; index avg `0.0097` n `23`; metal avg `0.7576` n `18`; unknown avg `0.4161` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
