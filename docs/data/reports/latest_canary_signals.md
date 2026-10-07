# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T03:37:29.611058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7903` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6233` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0181` n `13`; crypto_alt avg `0.1352` n `235`; crypto_major avg `0.1516` n `8`; equity avg `0.0477` n `150`; fx avg `0.0026` n `6`; index avg `0.0063` n `26`; metal avg `0.0316` n `20`; unknown avg `0.2228` n `1076`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `-0.2072` n `235`; crypto_major avg `0.1465` n `8`; equity avg `0.0768` n `150`; fx avg `-0.0109` n `6`; index avg `0.0029` n `26`; metal avg `-0.035` n `20`; unknown avg `3.0585` n `1074`
- 4h: commodity avg `0.165` n `13`; crypto_alt avg `-2.8207` n `235`; crypto_major avg `-1.8348` n `8`; equity avg `-0.5044` n `150`; fx avg `-0.0317` n `6`; index avg `-0.0445` n `26`; metal avg `-0.2115` n `20`; unknown avg `1.2009` n `1068`
- 24h: commodity avg `0.4513` n `13`; crypto_alt avg `-2.5734` n `235`; crypto_major avg `-2.0946` n `8`; equity avg `-0.0066` n `149`; fx avg `0.0674` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0622` n `20`; unknown avg `871.1051` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
