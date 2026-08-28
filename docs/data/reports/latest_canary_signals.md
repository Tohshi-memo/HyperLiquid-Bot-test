# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T05:37:24.393173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2348` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0696` n `12`; crypto_alt avg `0.3514` n `231`; crypto_major avg `0.3468` n `8`; equity avg `-0.0561` n `127`; fx avg `-0.0095` n `6`; index avg `-0.0107` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.9927` n `792`
- 1h: commodity avg `-0.0694` n `12`; crypto_alt avg `0.2377` n `231`; crypto_major avg `0.2938` n `8`; equity avg `-0.2896` n `127`; fx avg `-0.0155` n `6`; index avg `-0.0462` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.3528` n `792`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `-2.056` n `231`; crypto_major avg `-1.2901` n `8`; equity avg `-0.5998` n `127`; fx avg `-0.0124` n `6`; index avg `-0.0553` n `26`; metal avg `0.0071` n `20`; unknown avg `0.9706` n `792`
- 24h: commodity avg `0.295` n `12`; crypto_alt avg `0.9593` n `231`; crypto_major avg `1.8945` n `8`; equity avg `-0.2002` n `127`; fx avg `-0.0445` n `6`; index avg `0.0643` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.6188` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0575`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0534`, n `669`, weak_sample_signal
