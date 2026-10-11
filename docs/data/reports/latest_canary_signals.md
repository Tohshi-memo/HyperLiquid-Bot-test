# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T21:22:24.669091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0383` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `-0.5956` n `235`; crypto_major avg `-0.4512` n `8`; equity avg `-0.0456` n `150`; fx avg `0.0131` n `6`; index avg `-0.007` n `26`; metal avg `-0.0268` n `20`; unknown avg `0.8178` n `1130`
- 1h: commodity avg `0.0294` n `13`; crypto_alt avg `-0.8672` n `235`; crypto_major avg `-0.5311` n `8`; equity avg `-0.0613` n `150`; fx avg `-0.0145` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0249` n `20`; unknown avg `1.3399` n `1122`
- 4h: commodity avg `0.1367` n `13`; crypto_alt avg `-1.0425` n `235`; crypto_major avg `-1.0469` n `8`; equity avg `-0.0933` n `150`; fx avg `-0.0046` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0245` n `20`; unknown avg `1.421` n `1098`
- 24h: commodity avg `0.3518` n `13`; crypto_alt avg `0.7383` n `235`; crypto_major avg `0.0874` n `8`; equity avg `0.189` n `150`; fx avg `0.0139` n `6`; index avg `0.018` n `26`; metal avg `0.062` n `20`; unknown avg `0.6699` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
