# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T10:37:30.339863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0514` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.3197` n `235`; crypto_major avg `-0.3548` n `8`; equity avg `-0.0506` n `150`; fx avg `0.0199` n `6`; index avg `-0.0067` n `26`; metal avg `0.0096` n `20`; unknown avg `-0.0548` n `1076`
- 1h: commodity avg `0.077` n `13`; crypto_alt avg `-0.3078` n `235`; crypto_major avg `-0.3621` n `8`; equity avg `-0.0826` n `150`; fx avg `0.0179` n `6`; index avg `-0.0332` n `26`; metal avg `0.0036` n `20`; unknown avg `2.2954` n `1074`
- 4h: commodity avg `0.0889` n `13`; crypto_alt avg `-1.2955` n `235`; crypto_major avg `-1.1574` n `8`; equity avg `-0.6775` n `150`; fx avg `-0.0974` n `6`; index avg `-0.106` n `26`; metal avg `-0.2193` n `20`; unknown avg `1.2945` n `1058`
- 24h: commodity avg `1.2587` n `13`; crypto_alt avg `-4.7969` n `235`; crypto_major avg `-3.3049` n `8`; equity avg `-1.1115` n `150`; fx avg `-0.0866` n `6`; index avg `-0.2321` n `26`; metal avg `-0.4809` n `20`; unknown avg `815.1893` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
